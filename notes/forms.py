from django import forms
# from django.contrib.auth.models import 
from .models import Note, Tag
# from taggit.models import TagField



class CreateNote(forms.ModelForm):
# 	tags = forms.ModelMultipleChoiceField(
  #     queryset=Tag.objects.all(),
  #     widget=forms.CheckboxSelectMultiple


  # )

	class Meta:
		model = Note
		fields = ['title', 'content', 'tags']

		widgets = {
		'tags' : forms.CheckboxSelectMultiple()
		}

		

