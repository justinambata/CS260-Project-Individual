from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.core.urlresolvers import reverse

from todo.models import Item
from todo.forms import ItemForm

from itertools import chain
from datetime import date
from datetime import datetime, timedelta
import datetime

# Create your views here.
@login_required
def stat_info(request):
    return render_to_response('stat_info.html', {'is_auth':request.user.is_authenticated()}, context_instance=RequestContext(request))

@login_required
def mainmenu(request, action=None):
    """
    if(action == "updateitem"):
        _id = request.POST.get['_id']
        _status = request.POST.get['_status']
        item = Item.objects.get(id=_id)
        item.status = _status
        item.save()
    """
    loggedinuser = request.user.username
    today_min = datetime.datetime.combine(date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(date.today(), datetime.time.max)

    Item.objects.filter(owner=request.user.username).filter(created_date__lt=datetime.datetime.now()-timedelta(days=7)).delete()
	
    itemListToDo = Item.objects.filter(owner=request.user.username).filter(status=0)
    itemListSameDate = Item.objects.filter(owner=request.user.username).filter(~Q(status=0)).filter(created_date__range=(today_min, today_max))
    itemList = list(chain(itemListToDo, itemListSameDate))

    return render_to_response('mainmenu.html',{'itemList':itemList,'loggedinuser':loggedinuser}, context_instance=RequestContext(request))


@login_required
def updateitem(request, _id, _status):
    #_status = request.GET['_status']
    #_id = request.GET['_id']
    item = Item.objects.get(id=_id)
    item.status = _status
    item.save()
    return HttpResponseRedirect(reverse('mainmenu', args=(), kwargs={}))

"""
@login_required
def additem(request):
    loggedinuser = request.user.username
    return render_to_response('additem.html',{'loggedinuser':loggedinuser}, context_instance=RequestContext(request))
"""

@login_required
def additem(request):
    loggedinuser = request.user.username

    # Get the context from the request.
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        form = ItemForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            #form.save(commit=True)
            item = form.save(commit=False)
            item.owner = request.user.username
            item.save()

            # Now call the index() view.
            # The user will be shown the homepage.
            return mainmenu(request)
        #else:
            # The supplied form contained errors - just print them to the terminal.
            # print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = ItemForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    """
    return render_to_response('rango/add_category.html', {'form': form}, context)
    return render_to_response('additem.html',{'loggedinuser':loggedinuser, 'form': form}, context_instance=RequestContext(request))
    """
    return render_to_response('additem.html',{'loggedinuser':loggedinuser, 'form': form}, context)

"""
@login_required
def home_page(request):
    if request.user.is_authenticated():
        # Do something for authenticated users.
        loggedinuser = request.user.username
        loggedinmessage = 'You are logged in as <b>' + loggedinuser + '</b>.'
    else:
        # Do something for anonymous users.
        loggedinmessage = 'You are not currently logged in.'

    now = datetime.datetime.now()
    

    out_str = '<html>'
    out_str += '<title>To-Do lists</title>'
    out_str += '<body>'
    out_str += '<div id="divLoggedInMessage">' + loggedinmessage + '</div>'
    out_str += '<br />'
    out_str += '<div id="divCurrentDate">' + now.strftime("%B %d, %Y") + '</div>'
    out_str += '</body>'
    out_str += '</html>'

    return HttpResponse(out_str)
"""