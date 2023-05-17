from django.shortcuts import render
import requests
import openai
openai.api_key = "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"

def DISKUSI(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        model_engine = "text-davinci-003"

        completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            temperature=0.5,
        )

        message = completions.choices[0].text
        return render(request, "index.html", {"message": message})
    else:
        return render(request, "index.html")
