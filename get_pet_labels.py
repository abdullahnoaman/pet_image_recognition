#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Abdullah Noaman
# DATE CREATED:  06/23/2020                                
# REVISED DATE: 
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

# TODO 2: Define get_pet_labels function below please be certain to replace None
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
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    
    """start initiating a list for the file names and another list for the 
    labels that is empty for now"""
    filename_list = listdir(str(image_dir))
    pet_labels = []
    
    """use the filename_list data to fill pet_labels in the requested format"""
    for i in range(len(filename_list)):
        filename_in_list = filename_list[i].lower().split("_")
        petname = ""
        for word in filename_in_list:
            if word.isalpha():
                petname += word + " "
        petname = petname.strip()
        pet_labels += [petname]
        
    """create a dictionary to put the data in the two lists created in"""
    
    results_dic = dict()
    
    """if the file names from filename_list have not been added to the
    list yet, add them as a key and add values from pet_labels"""
    
    for i in range(len(filename_list)):
        if filename_list[i] not in results_dic:
            results_dic[filename_list[i]] = [pet_labels[i]] 
        else:
            print("** Warning: Key=", filename_list[i], 
               "already exists in results_dic with value =", 
               results_dic[filename_list[i]])

    
    
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
