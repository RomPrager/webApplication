from django import forms

class ContactForm(forms.forms):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        print(f'Sending email from {self.cleaned_data['email']} with message: {self.cleaned_data['message']}')

