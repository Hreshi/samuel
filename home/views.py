from django.shortcuts import render, redirect
# Create your views here.

SHOW_ERR = False
ROUND_NUM = 1
HINT_NUM = 1

def home(request):
	global SHOW_ERR, ROUND_NUM, HINT_NUM
	if request.method == "GET":
		SHOW_ERR = False
		ROUND_NUM = 1
		HINT_NUM = 1

	context = {
		"SHOW_ERR":0
	}
	if request.method == "POST":
		if request.POST["password"] == "smallpp":
			return redirect('/smallpp')
		else:
			SHOW_ERR = True

	if SHOW_ERR:
		context["SHOW_ERR"] = 1

	return render(request, 'home.html', context)


def hint(request):
	global HINT_NUM, hints
	allhints = ["VIEW SOURCE", "SHIFT BY 69", "SHOW IN THE MIRROR", "NO MORE HINTS YOU JERK"]

	if request.method == "POST":
		HINT_NUM += 1
	if HINT_NUM > len(allhints):
		HINT_NUM = len(allhints)

	hints = []
	for i in range(0, HINT_NUM):
		hints.append(allhints[i])

	context = {
		"hints" : hints,
		"HINT_NUM":HINT_NUM
	}
	return render(request, 'hints.html', context)

def smallpp(request):
	global ROUND_NUM
	context = {
		"ROUND_NUM" : ROUND_NUM
	}

	if request.method == "POST":
		ROUND_NUM += 1
	return render(request, 'smallpp.html', context)
