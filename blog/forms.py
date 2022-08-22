from django import forms
from blog.models import Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

# we can use FormHelper for change layout: https://django-crispy-forms.readthedocs.io/en/latest/layouts.html
class CommentForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(CommentForm, self).__init__(*args, **kwargs)
      self.helper = FormHelper()
      self.helper.add_input(Submit('submit', 'Submit'))


  class Meta:
    model = Comment
    fields = ['content']
    