from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect
import urllib.parse
import requests


key = "Ft7cfpVsK56Vn7lcUfPaU64PODTTekmt"

def index(request):
    return render(request, 'devops.html')

def submit(request):
    if request.method == 'POST':
        orig = request.POST.get('orig')
        dest = request.POST.get('dest')
        if "submit" in request.POST:
            if orig is not None and dest is not None:
                main_api = "https://www.mapquestapi.com/directions/v2/route?" 
                url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
                print("URL: " + (url))
            
                map_activity = ""
                data = dict()

                json_data = requests.get(url).json()
                json_status = json_data["info"]["statuscode"]
                if json_status == 0:
                    for each in json_data["route"]["legs"][0]["maneuvers"]:
                        map_activity += ((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)\n"))
                    data['map_activity'] = map_activity
                    return render(request, 'devops.html', data)
                elif json_status == 402:
                    print("**********************************************")
                    map_activity.append("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
                    print("**********************************************\n")
                    data['map_activity'] = map_activity
                    return render(request, 'devops.html', data)
                elif json_status == 611:
                    print("**********************************************")
                    map_activity.append("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
                    print("**********************************************\n")
                    data['map_activity'] = map_activity
                    return render(request, 'devops.html', data)
                else:
                    print("************************************************************************")
                    map_activity.append("For Staus Code: " + str(json_status) + "; Refer to:")
                    print("https://developer.mapquest.com/documentation/directions-api/status-codes")
                    print("************************************************************************\n")
                    data['map_activity'] = map_activity
                    return render(request, 'devops.html', data)
            else: 
                return messages.error(request, 'No Data Input')
        else:
            main_api = "https://www.mapquestapi.com/staticmap/v5/map?"
            mapurl = main_api + urllib.parse.urlencode({"key":key, "center":dest, "traffic":"flow"}) 
            urllib.request.urlretrieve(mapurl, "devops/static/image.jpg")  
            return redirect("http://127.0.0.1:8000/map")
    else:
        return HttpResponseRedirect(reverse('devops:index'))

def map(request):
    return render(request, 'map.html')