from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description", "due_date", "is_completed"]
        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "タスク名を入力してください"}
            ),
            "description": forms.Textarea(
                attrs={"placeholder": "詳細内容を入力してください"}
            ),
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }
