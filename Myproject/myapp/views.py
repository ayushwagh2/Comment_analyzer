# youtube_analysis/views.py
from django.shortcuts import render
from .utils import analyze_comments
from googleapiclient.errors import HttpError
from django import forms

class VideoLinkForm(forms.Form):
    video_link = forms.CharField(label="Enter YouTube Playlist Link", max_length=500)

def analyze_playlist_comments(request):
    results = None
    error_message = None
    form = VideoLinkForm()

    if request.method == 'POST':
        form = VideoLinkForm(request.POST)
        if form.is_valid():
            video_link = form.cleaned_data['video_link']
            # Extract the video ID from the link
            video_id = video_link.split("list=")[-1] 
            print(video_id)
             

            try:
                # Use the extracted video ID to analyze comments
                results = analyze_comments([video_id])  # Use a list for the video ID
            except HttpError as e:
                error_message = f"Error fetching comments: {e}"

    return render(request, 'myapp/analyze.html', {'form': form, 'results': results, 'error_message': error_message , 'rating_range': range(1, 11) })


# def analyze_playlist_comments(request):
#     results = None
#     error_message = None
#     hardcoded_playlist_id = "PLG-cz6t92P1EfPTlui349x3R0DdyZ-xB4"  # Hardcoded playlist ID for testing

#     try:
#         # Use the hardcoded playlist ID to analyze comments
#         results = analyze_comments([hardcoded_playlist_id])  # Use a list for the playlist ID
#     except HttpError as e:
#         error_message = f"Error fetching comments: {e}"

#     return render(request, 'myapp/results.html', {'results': results, 'error_message': error_message})


# from django.shortcuts import render, redirect
# from django.urls import reverse  # for generating URL for the redirect

# def analyze_playlist_comments(request):
#     results = None
#     error_message = None
#     form = VideoLinkForm()

#     if request.method == 'POST':
#         form = VideoLinkForm(request.POST)
#         if form.is_valid():
#             video_link = form.cleaned_data['video_link']
#             # Extract the video ID from the link
#             video_id = video_link.split("list=")[-1] 
#             print(video_id)
          
#             try:
#                 # Use the extracted video ID to analyze comments
#                 results = analyze_comments([video_id])  # Use a list for the video ID
#                 print(results[0])
                
#                 # Store results in the session
#                 request.session['average_sentiment'] = results[0]

#                 request.session['average_rating'] = results[1]
#                 request.session['comments'] = results[2].to_dict(orient='records')  # Convert DataFrame to list of dicts
                
#                 # Redirect to results page
#                 return redirect(reverse('results'))
            
#             except HttpError as e:
#                 error_message = f"Error fetching comments: {e}"

#     return render(request, 'myapp/analyze.html', {'form': form, 'error_message': error_message})


# def results(request):
#     # Get stored results from session
#     average_sentiment = request.session.get('average_sentiment')
#     average_rating = request.session.get('average_rating')
#     comments = request.session.get('comments', [])

#     # Render results template with session data
#     return render(request, 'myapp/results.html', {
#         'average_sentiment': average_sentiment,
#         'average_rating': average_rating,
#         'comments': comments
#     })