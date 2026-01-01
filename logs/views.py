from django.contrib.auth.decorators import login_required       # 로그인 확인 도구
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404  # HTML 그려주는 함수

from logs.forms import BodyLogForm
from logs.models import BodyLog                                 # BodyLog Model

# request는 Django가 만든 HttpRequest다. (규격봉투)
# request.user : 현재 로그인한 사용자
# request.method : 데이터를 달라는건지(GET) 저장하겠다는건지(POST)
# request.GET / request.POST : 사용자가 입력창에 적은 내용들
# request.FILES : 파일 데이터
# request.META : 접속자의 IP address, browser type (Chrome, Safari ..)

@login_required
def bodylog_list(request):
    # request.user : login user date
    logs = BodyLog.objects.filter(user=request.user).order_by('-date')
    context = { 'logs': logs, }
    return render(request, 'logs/bodylog_list.html', context)

@login_required
def bodylog_create(request):
    if request.method == 'POST':
        form = BodyLogForm(request.POST, request.FILES)
        if form.is_valid():
            log = form.save(commit=False)
            log.user = request.user
            log.save()
            return redirect('logs:index')
    else:
        last_log = BodyLog.objects.filter(user=request.user).order_by('-date').first()
        initial_data = {}
        if last_log:
            initial_data = {
                'height': last_log.height,
                'weight': last_log.weight,
            }
        form = BodyLogForm(initial=initial_data)
    return render(request, 'logs/bodylog_form.html', {'form': form})

@login_required
def bodylog_edit(request, pk):
    log = get_object_or_404(BodyLog, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BodyLogForm(request.POST, request.FILES, instance=log)
        if form.is_valid():
            form.save()
            return redirect('logs:index')
    else:
        form = BodyLogForm(instance=log)
    return render(request, 'logs/bodylog_form.html', {'form': form, 'is_edit': True})

@login_required
def bodylog_delete(request, pk):
    log = get_object_or_404(BodyLog, pk=pk, user=request.user)
    if request.method == 'POST':
        log.delete()
    return redirect('logs:index')

def log_detail_api(request, pk):
    try:
        log = BodyLog.objects.get(pk=pk, user=request.user)
        return JsonResponse({
            'front': log.image_front.url if log.image_front else '',
            'side': log.image_side.url if log.image_side else '',
            'back': log.image_back.url if log.image_back else '',
            'date': log.date.strftime('%Y-%m-%d'),
            'bmi': log.bmi
        })
    except BodyLog.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)