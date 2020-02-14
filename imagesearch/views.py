from django.http import JsonResponse
import json
from django.shortcuts import render
import flickrapi

def home(request):    
        api_key = ""
        secret_api_key = ""
        flickr = flickrapi.FlickrAPI(api_key, secret_api_key)
        keyword = "sun set"
        photo_list = flickr.photos.search(api_key=api_key, text=keyword, per_page=52, page=1, safe_search=1, format='parsed-json')
        imgurllist=[]
        total_imgs = len(photo_list['photos']['photo'])  # the number of images per page is not always exactly 52 (flickr bug)
        rng = total_imgs if total_imgs < 52 else 52
        for i in range(rng):
            farmid=photo_list['photos']['photo'][i]['farm']
            serverid=photo_list['photos']['photo'][i]['server']
            id=photo_list['photos']['photo'][i]['id']
            secret=photo_list['photos']['photo'][i]['secret']
            imgurllist.append(f"https://farm{farmid}.static.flickr.com/{serverid}/{id}_{secret}.jpg")           
        print(imgurllist)
        return render (request, "home.html", {'imgurl':imgurllist})

def search_result(request):
    
    if request.method == "GET":                         
        searchkey = request.GET.get('search')
        api_key = ""
        secret_api_key = ""
        flickr = flickrapi.FlickrAPI(api_key, secret_api_key)
        photo_list = flickr.photos.search(api_key=api_key, text=searchkey, per_page=52, page=1, safe_search=1, format='parsed-json')
        totalpages = int(photo_list['photos']['pages'])          
        total_imgs_current_page = len(photo_list['photos']['photo'])
        rng = total_imgs_current_page if total_imgs_current_page < 52 else 52
        imgurllist=[]
        for i in range(rng):
            farmid=photo_list['photos']['photo'][i]['farm']
            serverid=photo_list['photos']['photo'][i]['server']
            id=photo_list['photos']['photo'][i]['id']
            secret=photo_list['photos']['photo'][i]['secret']
            imgurllist.append(f"https://farm{farmid}.static.flickr.com/{serverid}/{id}_{secret}.jpg")
            
            # imgurllist = ["File:///C:\\Users\\Admin\\Pictures\\p\\1.jpg","File:///C:\\Users\\Admin\\Pictures\\p\\2.jpg","File:///C:\\Users\\Admin\\Pictures\\p\\3.jpg","File:///C:\\Users\\Admin\\Pictures\\p\\4.jpg"]   
                      # delete this line
        context = {
                'imgurl':imgurllist , 
                'numofpages' : totalpages
        }
        return render (request, "search_results.html", context)

def ajax(request):
    if request.is_ajax():
            result = request.GET.get('pageNumber')
            searchkey = request.GET.get('search')
            num= result
            print(result)
            api_key = ""
            secret_api_key = ""
            flickr = flickrapi.FlickrAPI(api_key, secret_api_key)
            photo_list = flickr.photos.search(api_key=api_key, text=searchkey, per_page=52, page=num, tag="",safe_search=1, format='parsed-json')
            totalpages = int(photo_list['photos']['pages'])          
            total_imgs_current_page = len(photo_list['photos']['photo'])
            rng = total_imgs_current_page if total_imgs_current_page < 52 else 52
            imgurllist=[]
            for i in range(rng):
                farmid=photo_list['photos']['photo'][i]['farm']
                serverid=photo_list['photos']['photo'][i]['server']
                id=photo_list['photos']['photo'][i]['id']
                secret=photo_list['photos']['photo'][i]['secret']
                imgurllist.append(f"https://farm{farmid}.static.flickr.com/{serverid}/{id}_{secret}.jpg")
            
            
            
            return JsonResponse(imgurllist, safe=False)           


