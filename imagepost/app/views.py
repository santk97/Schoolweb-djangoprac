from django.shortcuts import render,HttpResponse,redirect
from .models import  PostModel
from .forms import PostForm
from imgurpython import ImgurClient

id='4b3c0ba3c9adf95'
secret='1b959c428010f4f10b55510b81531c037f070c95'
# Create your views here.

def post_view(request):
        if request.method=='GET':
            form=PostForm()
        elif request.method=='POST':
            form=PostForm(request.POST,request.FILES)
            if form.is_valid():
                image=form.cleaned_data.get('image')
                caption=form.cleaned_data.get('caption')
                print('the imagr is ',image)
                post=PostModel(image=image,caption=caption)
                post.save()
                path = post.image.url
                print('the path is ',path)
                #post.image_url=path
                client = ImgurClient(id, secret)
                # using the imgur API to upload the posts to the imgur servers
                image_url = client.upload_from_path('.'+path,anon=True)['link']
                print(image_url)
                post.image_url=image_url
                post.save()
                return redirect('/app/')
            return render(request,'post.html',{'form':form})



def feed_view(request):
        posts = PostModel.objects.all().order_by('-created_on')
        return render(request, 'feed.html', {'posts': posts})

