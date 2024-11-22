from django import forms


from .models import CommentSectionModel, Post

class CommentSectionForm(forms.ModelForm):
    class Meta:
        model = CommentSectionModel
        fields = "__all__"
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }


class AddNewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        labels = {
            "title" : "Tittle",
            "first_name" : "Nome Autore",
            "last_name" : "Cognome Autore",
            "e_mail_address" : "E-mail Atuore",
            "excerpt" : "Excerpt",
            "image_name": "Immagine",
            "slug" : "Slug",
            "content" : "Contenuto",
            "caption" : "Tag",
        }