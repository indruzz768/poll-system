from django.shortcuts import render, get_object_or_404, redirect
from .models import Poll, Option, Vote
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from django.db.models import F, Q
from django.utils import timezone


def poll_list(request):
    now = timezone.now()
    polls = Poll.objects.filter(is_active=True).filter(
        Q(expiry_date__gt=now) | Q(expiry_date__isnull=True)
    ).order_by('-created_at')
    return render(request, 'polls/poll_list.html', {'polls': polls})

def poll_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    # check if user already voted
    user_voted = False
    if request.user.is_authenticated:
        user_voted = Vote.objects.filter(user=request.user, poll=poll).exists()
    return render(request, 'polls/poll_detail.html', {'poll': poll, 'user_voted': user_voted})

@login_required
def poll_vote(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    if request.method != 'POST':
        return redirect('polls:poll_detail', pk=pk)

    # prevent voting twice
    if Vote.objects.filter(user=request.user, poll=poll).exists():
        messages.error(request, "You have already voted in this poll.")
        return redirect('polls:poll_results', pk=pk)

    option_id = request.POST.get('option')
    try:
        option = poll.options.get(pk=option_id)
    except Option.DoesNotExist:
        messages.error(request, "Invalid option.")
        return redirect('polls:poll_detail', pk=pk)

    # create vote and increment option.votes atomically
    with transaction.atomic():
        Vote.objects.create(user=request.user, poll=poll, option=option)
        # increment counter safely
        Option.objects.filter(pk=option.pk).update(votes=F('votes') + 1)

    return redirect('polls:poll_results', pk=pk)


def poll_results(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    options = poll.options.all()
    total = sum(o.votes for o in options)
    # calculate percentages (avoid divide by zero)
    results = []
    for o in options:
        pct = (o.votes / total * 100) if total > 0 else 0
        results.append({'text': o.text, 'votes': o.votes, 'pct': round(pct, 2)})
    return render(request, 'polls/poll_results.html', {'poll': poll, 'results': results, 'total': total})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created. Please log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def my_votes(request):
    votes = Vote.objects.select_related('poll', 'option').filter(user=request.user).order_by('-created_at')
    return render(request, 'polls/my_votes.html', {'votes': votes})
