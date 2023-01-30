from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import random


# Create your views here.
def home(request):
    hadith = {
        1: '1Gabriel did not come to the Prophet (for some time) and so one of the Quraish women said, "His Satan has deserted him." So came the Divine Revelation: "By the forenoon And by the night When it is still! Your Lord (O Muhammad) has neither Forsaken you Nor hated you." (93.1-3)',
        2: '2Gabriel did not come to the Prophet (for some time) and so one of the Quraish women said, "His Satan has deserted him." So came the Divine Revelation: "By the forenoon And by the night When it is still! Your Lord (O Muhammad) has neither Forsaken you Nor hated you." (93.1-3)',
        3: '3Gabriel did not come to the Prophet (for some time) and so one of the Quraish women said, "His Satan has deserted him." So came the Divine Revelation: "By the forenoon And by the night When it is still! Your Lord (O Muhammad) has neither Forsaken you Nor hated you." (93.1-3)',
        4: '4Gabriel did not come to the Prophet (for some time) and so one of the Quraish women said, "His Satan has deserted him." So came the Divine Revelation: "By the forenoon And by the night When it is still! Your Lord (O Muhammad) has neither Forsaken you Nor hated you." (93.1-3)',
        5: '5Gabriel did not come to the Prophet (for some time) and so one of the Quraish women said, "His Satan has deserted him." So came the Divine Revelation: "By the forenoon And by the night When it is still! Your Lord (O Muhammad) has neither Forsaken you Nor hated you." (93.1-3)',
    }
    
    references = {
        1: 'Book 2, Hadith 4',
        2: 'Book 12, Hadith 4',
        3: 'Book 22, Hadith 4',
        4: 'Book 32, Hadith 4',
        5: 'Book 42, Hadith 4',
    }
    
    random_key = random.choice(list(hadith.keys()))
    
    random_hadithtext = hadith[random_key]
    random_reference = references[random_key]
    return render(
        request, "home.html", {"random_key": random_key, "random_value": random_hadithtext, "random_reference":random_reference}
    )


# def my_view(request):

#     return render(request, 'mytemplate.html', {'random_key': random_key, 'random_value': random_value})
