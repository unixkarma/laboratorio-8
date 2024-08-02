from django import forms
from .models import Trainer, Pokemon


class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'
        widgets = {

                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'type': forms.Select(attrs={'class': 'form-control'}),
                'weight': forms.TextInput(attrs={'class': 'form-control'}),
                'height': forms.TextInput(attrs={'class': 'form-control'}),
                'trainer': forms.Select(attrs={'class': 'form-control'}),
                'picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
                }

class TrainerForm(forms.ModelForm):                                                            
    class Meta:                                                                                 
        model = Pokemon                                                                         
        fields = '__all__'                                                                      
        widgets = {                                                                             
                                                                                                
                'name': forms.TextInput(attrs={'class': 'form-control'}),                       
                'type': forms.Select(attrs={'class': 'form-control'}),                          
                'weight': forms.TextInput(attrs={'class': 'form-control'}),                     
                'height': forms.TextInput(attrs={'class': 'form-control'}),                     
                'trainer': forms.Select(attrs={'class': 'form-control'}),                       
                'picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'})       
                }                                                                               
   
