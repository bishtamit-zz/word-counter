from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    wordlist = fulltext.split()

    wc_dict = dict()

    for word in wordlist:
        if word in wc_dict:
            wc_dict[word] += 1
        else:
            wc_dict[word] = 1
    wc_dict = sorted(wc_dict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'frequency': dict(wc_dict[:10])})

def about(request):
    return render(request, 'about.html')