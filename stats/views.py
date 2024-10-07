from django.shortcuts import render

def posts_list(request):
  return render(request, 'stats/stats_list.html')