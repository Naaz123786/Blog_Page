from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect

from .models import Post, CommentSectionModel
from .forms import CommentSectionForm, AddNewPostForm


# Create your views here.
def starting_page(request):
    latest_posts  = Post.objects.all().order_by("-date")[:3]
    mostview_posts = Post.objects.all().order_by("-views")[:3]
    mostlike_posts = Post.objects.all().order_by("-like")[:3]
    mostcomment_posts = Post.objects.all().order_by("-comments")[:3]

    request.session['page_type'] = 'index'
    request.session.save()

    return render(request, "blogs/index.html", {
        "posts": latest_posts,
        "session": request.session, 
        "view_post": mostview_posts,
        "like_post": mostlike_posts,
        "comment_post": mostcomment_posts,
        "page_type": request.session['page_type']
    })

def posts(request):
    all_posts = Post.objects.all().order_by("-date")

    request.session['page_type'] = 'all_posts'
    request.session.save()

    return render(request, "blogs/all-posts.html",{
        "all_posts": all_posts,
        "session": request.session,
        "page_type" : request.session['page_type']
    })

class AddPostView(View):
    def get(self, request):
        model = Post
        form = AddNewPostForm
        return render(request, "blogs/add_post.html", {
            "form": form,
            "model": model
        })
    
    def post(self, request):
        submitted = request.POST
        model = Post
        form = AddNewPostForm

        user_submitted = Post(
            title = submitted['title'],
            first_name = submitted['first_name'],
            last_name = submitted['last_name'],
            e_mail_address = submitted['e_mail_address'],
            excerpt = submitted['excerpt'],
            image= request.FILES["image"],
            slug = submitted['slug'],
            content = submitted['content'] ,
            caption = submitted['caption'],
        ) 
        user_submitted.save()
        return render(request, "blogs/add_post.html",{
            "form": form,
            "model": model,
        })

class post_detail(View):
    def get(self, request, slug):
        form = CommentSectionForm
        model = CommentSectionModel
        identified_post = get_object_or_404(Post, slug=slug)
        all_comment = CommentSectionModel.objects.filter(slug=slug)

        view = Post.objects.get(slug=slug)
        view.views += 1
        view.save()

        return render(request, "blogs/post-details.html",{
            "post_details": identified_post,
            "post_tags": identified_post.caption ,
            "form": form,
            "model": model,
            "comments": all_comment,
            "session": request.session,
        })

    def post(self, request, slug):
        submitted_data = request.POST
        form = CommentSectionForm
        model = CommentSectionModel
        user_comment = CommentSectionModel(
            nome_utente = submitted_data['nome_utente'],
            rating = submitted_data['rating'],
            commento = submitted_data['commento'],
            slug = slug
        )
        user_comment.save()

        comment = Post.objects.get(slug=slug)
        comment.comments += 1
        comment.save()

        all_comment = CommentSectionModel.objects.filter(slug=slug)
        identified_post = get_object_or_404(Post, slug=slug)
        return render(request, "blogs/post-details.html", {
            "form": form,
            "model": model,
            "comments": all_comment,
            "post_details": identified_post,
            "post_tags": identified_post.caption,
            "session": request.session,
        })
    
class ReadLaterView(View):
    def post(self, request):
        post_slug = request.POST["slug"]
        request.session[f"{post_slug}"] = post_slug
        latest_posts  = Post.objects.all().order_by("-date")[:3]
        mostview_posts = Post.objects.all().order_by("-views")[:3]
        mostlike_posts = Post.objects.all().order_by("-like")[:3]
        mostcomment_posts = Post.objects.all().order_by("-comments")[:3]

        page_type = request.session['page_type']
        print(page_type)

        if page_type == "index":
            
            return render(request, "blogs/index.html", {
                "posts": latest_posts,
                "session": request.session, 
                "view_post": mostview_posts,
                "like_post": mostlike_posts,
                "comment_post": mostcomment_posts
            })
        
        elif page_type == "all_posts":

            all_posts = Post.objects.all().order_by("-date")
            return render(request, "blogs/all-posts.html", {
                "all_posts": all_posts,
                "session": request.session,
                "page_type" : request.session['page_type']
            })

class AllReadLaterView(View):
    def get(self, request):
        slug_values = []

        for keys in request.session.keys():
            if Post.objects.filter(slug=keys):
                slug_values.append(keys)
        all_posts = Post.objects.filter(slug__in=slug_values)
      
        if len(slug_values) == 0:
            return render(request, "blogs/readlater.html",{
            "all_posts": all_posts,
            "session": request.session,
            "message": "You have not saved any posts"
        })
        
        else:
            return render(request, "blogs/readlater.html",{
                "all_posts": all_posts,
                "session": request.session,
            })
    
class DeleteView(View):
    
    def post(self, request):
        slug_values = request.POST['slug']

        del request.session[slug_values]
    
        if request.session['page_type'] == 'index':

            latest_posts  = Post.objects.all().order_by("-date")[:3]
            mostview_posts = Post.objects.all().order_by("-views")[:3]
            mostlike_posts = Post.objects.all().order_by("-like")[:3]
            mostcomment_posts = Post.objects.all().order_by("-comments")[:3]

            return render(request, "blogs/index.html", {
                "posts": latest_posts,
                "session": request.session, 
                "view_post": mostview_posts,
                "like_post": mostlike_posts,
                "comment_post": mostcomment_posts,
                "page_type": request.session['page_type']
            })
        
        elif request.session['page_type'] == 'all_posts':
            all_posts = Post.objects.all().order_by("-date")

            request.session['page_type'] = 'all_posts'
            request.session.save()

            return render(request, "blogs/all-posts.html",{
                "all_posts": all_posts,
                "session": request.session,
                "page_type" : request.session['page_type']
            })