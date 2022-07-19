from django import forms

class CreateNewList(forms.Form):
    
    name = forms.CharField(label="Name", max_length=200 )
    check = forms.BooleanField(required=False)
    
    
    
    
    #in our create.html when we denoting our form to any place
    #{{form}}like this we can use diffrent layout of showing these
    #forms example {{forms.as_p}} or {{forms.as_ul}}
    #for horizontal alignment of form and we can manipulate it 
    #structure via this.
    
    #make sure you add {% csrf_token %} for security measures of form 
    #to avoid getting error 403 (forbidden security key)