from django.shortcuts import render
def power(request):
    pwr = ''
    if request.method == "POST":
        intensity=float(request.POST.get("int"))
        resistance=float(request.POST.get("res"))
        pwr=(intensity**2)*resistance
        print(f"Intensity: {intensity}\nResistance: {resistance}\nPower: {pwr:.2f}")
    return render(request,'calcpower.html',{'Power':pwr})