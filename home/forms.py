from django import forms


class ContactForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "input input-bordered bg-base-100 border-base-300 focus:border-primary rounded-xl w-full",
                "placeholder": "Tu nombre",
            }
        ),
        label="Nombre",
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "input input-bordered bg-base-100 border-base-300 focus:border-primary rounded-xl w-full",
                "placeholder": "tu@correo.com",
            }
        ),
        label="Correo electrónico",
    )
    mensaje = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "textarea textarea-bordered bg-base-100 border-base-300 focus:border-primary rounded-xl w-full h-36 resize-none",
                "placeholder": "¿En qué podemos ayudarte?",
            }
        ),
        label="Mensaje",
    )

    newsletter_opt_in = forms.BooleanField(
        required=False,
        initial=True,
        label="Acepto recibir noticias y novedades ocasionales.",
        widget=forms.CheckboxInput(
            attrs={"class": "checkbox checkbox-xs checkbox-primary rounded"}
        ),
    )

    hp_website = forms.CharField(
        required=False,
        widget=forms.HiddenInput(attrs={"class": "hidden", "autocomplete": "off"}),
    )

    form_timestamp = forms.CharField(
        widget=forms.HiddenInput(),
    )
