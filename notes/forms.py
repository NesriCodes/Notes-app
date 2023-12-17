from django import forms
from .models import Note, Tag
from ckeditor.widgets import CKEditorWidget



class CreateNote(forms.ModelForm):
	content = forms.CharField(widget=CKEditorWidget())
	class Meta:
		model = Note
		fields = ['title', 'content', 'tags']

		widgets = {
		'tags' : forms.CheckboxSelectMultiple()
		}

		

