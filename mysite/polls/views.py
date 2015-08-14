from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Question

# Create your views here.
def index(request):
	# OPTION 1: Returning static text
	#return HttpResponse("Hello, world. You're at the polls index.")
	# OPTION 2: Returning dynamic content
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#output = ', '.join([p.question_text for p in latest_question_list])
	#return HttpResponse(output)
	# OPTION 3: Handing markup over to template
	#template = loader.get_template('polls/index.html')
	#context = RequestContext(request, {
	#	'latest_question_list': latest_question_list,
	#})
	#return HttpResponse(template.render(context))
	# OPTION 4: Handing markup over to template using shortcut
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)
	
def detail(request, question_id):
	# OPTION 1: Returning static text
	#return HttpResponse("You're looking at question %s." % question_id)
	# OPTION 2: Returning dynamic content
	#try:
	#	question = Question.objects.get(pk=question_id)
	#except Question.DoesNotExist:
	#	raise Http404("Question does not exist")
	#return render(request, 'polls/detail.html', {'question': question})
	# OPTION 3: Returning dynamic content, using shortcut
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)
