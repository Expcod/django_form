
from django.shortcuts import render
from .forms import MyForm

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Foydalanuvchidan ma'lumotlarni qabul qilish
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # Ma'lumotlarni ma'lumotlar bazasiga saqlash yoki boshqa operatsiyalar
            return render(request, 'success.html')
    else:
        form = MyForm()
    return render(request, 'my_template.html', {'form': form})
