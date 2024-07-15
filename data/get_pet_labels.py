#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Werner Koegelenberg
# DATE CREATED: 5 July 2024                                  
# REVISED DATE: 15 July 2024
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below, please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains the following item:
         index 0 = pet image label (string)
    """
    # Get the list of filenames in the specified directory
    filename_list = listdir(image_dir)
    
    # Initialize an empty dictionary to store the results
    results_dic = dict()
    
    # Iterate through each file in the directory
    for filename in filename_list:
        # Skip hidden files (those starting with a dot)
        if filename[0] != ".":
            # Split the filename by underscores and convert to lowercase
            word_list = filename.lower().split('_')
            # Initialize pet name as an empty string
            pet_name = ''
            
            # Iterate through each word in the split filename
            for word in word_list:
                # Check if the word is alphabetic
                if word.isalpha():
                    # Append the word to pet name with a space
                    pet_name += word + " "
            
            # Strip leading and trailing whitespace from pet name
            pet_name = pet_name.strip()
            
            # Check if the filename is already in the dictionary
            if filename not in results_dic:
                # Add the filename and pet name to the dictionary
                results_dic[filename] = [pet_name]
            else:
                print("** Warning: Duplicate files exist in directory:", filename)
    
    # Return the results_dic dictionary
    return results_dic