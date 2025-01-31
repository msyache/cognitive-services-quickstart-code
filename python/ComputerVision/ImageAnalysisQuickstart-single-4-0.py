# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.

# Azure AI Vision SDK -- Python Image Analysis Quickstart

# <snippet_single>
import azure.ai.vision as visionsdk

# Replace the string "PASTE_YOUR_COMPUTER_VISION_ENDPOINT_HERE" with your Computer Vision endpoint, found in the Azure portal.
# The endpoint has the form "https://<your-computer-vision-resource-name>.cognitiveservices.azure.com".
# Replace the string "PASTE_YOUR_COMPUTER_VISION_SUBSCRIPTION_KEY_HERE" with your Computer Vision key. The key is a 32-character
# HEX number (no dashes), found in the Azure portal. Similar to "d0dbd4c2a93346f18c785a426da83e15".
computer_vision_endpoint, computer_vision_key = "PASTE_YOUR_COMPUTER_VISION_ENDPOINT_HERE", "PASTE_YOUR_COMPUTER_VISION_SUBSCRIPTION_KEY_HERE"

service_options = visionsdk.VisionServiceOptions(endpoint=computer_vision_endpoint, key=computer_vision_key)

# Specify the URL of the image to analyze
image_url = "https://learn.microsoft.com/azure/cognitive-services/computer-vision/media/quickstarts/presentation.png"
vision_source = visionsdk.VisionSource(url=image_url)

# Set the language and one or more visual features as analysis options
image_analysis_options =  visionsdk.ImageAnalysisOptions()
image_analysis_options.features = (
    visionsdk.ImageAnalysisFeature.CAPTIONS
    | visionsdk.ImageAnalysisFeature.TEXT
)

# Create the image analyzer object
image_analyzer = visionsdk.ImageAnalyzer(service_options=service_options, vision_source=vision_source, image_analysis_options=image_analysis_options)

# Do image analysis for the specified visual features
result = image_analyzer.analyze()

# Checks result.
if result.reason == visionsdk.ImageAnalysisResultReason.ANALYZED:
    if result.captions is not None:
        print(' Captions:')
        for caption in result.captions:
            print('   \'{}\', Confidence {:.4f}'.format(caption.content, caption.confidence))
    if result.text is not None:
        print(' Text:')
        for line in result.text.lines:
            points_string = '{' + ', '.join([str(int(point)) for point in line.bounding_polygon]) + '}'
            print('   Line: \'{}\', Bounding polygon {}'.format(line.content, points_string))
            for word in line.words:
                points_string = '{' + ', '.join([str(int(point)) for point in word.bounding_polygon]) + '}'
                print('     Word: \'{}\', Bounding polygon {}, Confidence {:.4f}'
                        .format(word.content, points_string, word.confidence))
    
elif args.result.reason == visionsdk.ImageAnalysisResultReason.ERROR:
    error_details = visionsdk.ImageAnalysisErrorDetails.from_result(args.result)
    print(" Analysis failed.")
    print("   Error reason: {}".format(error_details.reason))
    print("   Error code: {}".format(error_details.error_code))
    print("   Error message: {}".format(error_details.message))
    print(" Did you set the computer vision endpoint and key?")
# </snippet_single>