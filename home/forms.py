from django import forms


class ContactForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "input input-bordered w-full", "placeholder": "Tu nombre"}
        ),
        label="Nombre",
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "input input-bordered w-full",
                "placeholder": "tu@correo.com",
            }
        ),
        label="Correo electrónico",
    )
    mensaje = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "textarea textarea-bordered w-full h-32",
                "placeholder": "¿En qué podemos ayudarte?",
            }
        ),
        label="Mensaje",
    )

    hp_website = forms.CharField(
        required=False,
        widget=forms.HiddenInput(attrs={"class": "hidden", "autocomplete": "off"}),
    )

    form_timestamp = forms.CharField(
        widget=forms.HiddenInput(),
    )
