#!/usr/bin/env python
# coding: utf-8

"""
Program (Python 3.8) for extracting results of the SAPT analysis (originated from Psi4 software) including: electrostatics, exchange, induction, dispersion, and total sapt0 terms.
Directories along with data within sould be extracted and placed into the same location as the python program.

Usage:  python3.8 sapt_energy_extraction_data.py

@author: Jacek Kujawski
"""

import os, re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

path = 'D:\\Coronavirus\\6VYO\\docked_first_poses\\6VYO_Zn\\complex\\SAPT\\Nprx_proba'
dirfiles = os.listdir(path)

fullpaths = map(lambda name: os.path.join(path, name), dirfiles)

dirs = []
electrostatics_list = []
exchange_list = []
induction_list = []
dispersion_list = []
total_sapt0_list = []
contacts = []

def extracting_data():
    for directory in fullpaths:
        if os.path.isdir(directory): dirs.append(directory)

    for directory in dirs:
        with open(f"{directory}/sapt0.out","r") as f:
            lines = f.readlines()
            for i in range(len(lines)):
                if 'Electrostatics          ' in lines[i]:
                    lines[i] = re.findall(r"[-+]?\d*\.\d+|\d+", lines[i])
                    print(directory.split("\\")[-1], ": ", "Electrostatics: ", round(float(lines[i][1]), 5), "kcal/mol")
                    electrostatics_list.append(round(float(lines[i][1]), 5))
                    contacts.append(directory.split("\\")[-1])

                if 'Exchange          ' in lines[i]:
                    lines[i] = re.findall(r"[-+]?\d*\.\d+|\d+", lines[i])
                    print(directory.split("\\")[-1], ": ", "Exchange: ", round(float(lines[i][1]), 5), "kcal/mol")
                    exchange_list.append(round(float(lines[i][1]), 5))
                    

                if 'Induction          ' in lines[i]:
                    lines[i] = re.findall(r"[-+]?\d*\.\d+|\d+", lines[i])
                    print(directory.split("\\")[-1], ": ", "Induction: ", round(float(lines[i][1]), 5), "kcal/mol")
                    induction_list.append(round(float(lines[i][1]), 5))
                    

                if 'Dispersion          ' in lines[i]:
                    lines[i] = re.findall(r"[-+]?\d*\.\d+|\d+", lines[i])
                    print(directory.split("\\")[-1], ": ", "Dispersion: ", round(float(lines[i][1]), 5), "kcal/mol")
                    dispersion_list.append(round(float(lines[i][1]), 5))
                    

                if 'Total SAPT0          ' in lines[i]:
                    lines[i] = re.findall(r"[-+]?\d*\.\d+|\d+", lines[i])
                    print(directory.split("\\")[-1], ": ", "Total SAPT0: ", round(float(lines[i][1]), 5), "kcal/mol")
                    total_sapt0_list.append(round(float(lines[i][1]), 5))
                    
                else:
                    continue

def eletrostatics_plot():
    labels = contacts
    values = electrostatics_list

    plt.figure(figsize=(18,9), dpi=300)
    plt.xlabel('Contacts')
    plt.ylabel('Electrostatics [kcal/mol]')
    col_map = plt.get_cmap('Paired')
    bars = plt.bar(labels, values, color=col_map.colors, edgecolor='k',width=0.5)
    for bar in bars:
        plt.annotate(bar.get_height(), 
                     xy=(bar.get_x(), bar.get_height()), 
                     fontsize=10)
    plt.xticks(rotation=90)
    plt.savefig('sapt_electrostatics.tiff', dpi=300)
    plt.show()    

    
def exchange_plot():
    labels = contacts
    values = exchange_list

    plt.figure(figsize=(18,9), dpi=300)
    plt.xlabel('Contacts')
    plt.ylabel('Exchange [kcal/mol]')
    col_map = plt.get_cmap('Paired')
    bars = plt.bar(labels, values, color=col_map.colors, edgecolor='k',width=0.5)
    for bar in bars:
        plt.annotate(bar.get_height(), 
                     xy=(bar.get_x(), bar.get_height()), 
                     fontsize=10)
    plt.xticks(rotation=90)
    plt.savefig('sapt_exchange.tiff', dpi=300)
    plt.show()

def induction_plot():
    labels = contacts
    values = induction_list

    plt.figure(figsize=(18,9), dpi=300)
    plt.xlabel('Contacts')
    plt.ylabel('Induction [kcal/mol]')
    col_map = plt.get_cmap('Paired')
    bars = plt.bar(labels, values, color=col_map.colors, edgecolor='k',width=0.5)
    for bar in bars:
        plt.annotate(bar.get_height(), 
                     xy=(bar.get_x(), bar.get_height()), 
                     fontsize=10)
    plt.xticks(rotation=90)
    plt.savefig('sapt_induction.tiff', dpi=300)
    plt.show()   
    
def dispersion_plot():
    labels = contacts
    values = dispersion_list

    plt.figure(figsize=(18,9), dpi=300)
    plt.xlabel('Contacts')
    plt.ylabel('Dispersion [kcal/mol]')
    col_map = plt.get_cmap('Paired')
    bars = plt.bar(labels, values, color=col_map.colors, edgecolor='k',width=0.5)
    for bar in bars:
        plt.annotate(bar.get_height(), 
                     xy=(bar.get_x(), bar.get_height()), 
                     fontsize=10)
    plt.xticks(rotation=90)
    plt.savefig('sapt_dispersion.tiff', dpi=300)
    plt.show()

def total_sapt0_plot():
    labels = contacts
    values = total_sapt0_list

    plt.figure(figsize=(18,9), dpi=300)
    plt.xlabel('Contacts')
    plt.ylabel('Total SAPT0 [kcal/mol]')
    col_map = plt.get_cmap('Paired')
    bars = plt.bar(labels, values, color=col_map.colors, edgecolor='k',width=0.5)
    for bar in bars:
        plt.annotate(bar.get_height(), 
                     xy=(bar.get_x(), bar.get_height()), 
                     fontsize=10)
    plt.xticks(rotation=90, fontsize=8)
    plt.savefig('sapt_total_sapt0.tiff', dpi=300)
    plt.show()  

def excel_write():
    df = pd.DataFrame({
        'Contacts':      contacts,
        'Eletrostatics': electrostatics_list,
        'Echange':       exchange_list,
        'Induction':     induction_list,
        'Dispersion':    dispersion_list,
        'Total SAPT0':    total_sapt0_list})
    df = df[['Contacts', 'Eletrostatics', 'Echange', 'Induction', 'Dispersion', 'Total SAPT0']]
    writer = pd.ExcelWriter('sapt_energy_calculations.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', startrow=1, header=False, index=False)
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    (max_row, max_col) = df.shape
    column_settings = [{'header': column} for column in df.columns]
    worksheet.add_table(0,0,max_row,max_col-1, {'columns': column_settings})
    writer.save()

extracting_data()
eletrostatics_plot()
exchange_plot()
induction_plot()
dispersion_plot()
total_sapt0_plot()
excel_write()

