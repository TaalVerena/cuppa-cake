from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Flavour


class ProductForm(forms.ModelForm):
    """
    Form for creating and updating Product instances.
    """

    class Meta:
        model = Product
        fields = "__all__"  # Include all fields from the Product model

    image = forms.ImageField(
        label="Image",
        required=False,
        widget=CustomClearableFileInput,  # Custom widget for image upload
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Populate category choices with friendly names
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields["category"].choices = friendly_names

        # Populate flavour choices with friendly names
        flavours = Flavour.objects.all()
        flavour_names = [(f.id, f.friendly_name or f.name) for f in flavours]
        self.fields["flavour"].choices = flavour_names

        # Add a CSS class to all form fields
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"
