# Frater by Alex Arbuckle #

import xlwt, xlrd
import os, time, discord
from xlutils.copy import copy
from selenium import webdriver
from discord.ext import commands

id = 'Frater'
driver = webdriver.Chrome()
client = commands.Bot(command_prefix = '{} '.format(id))
token = ''

@client.command()
async def Write(ctx, arg):
    '''  '''

    driver.get(ctx.message.attachments[0].url), time.sleep(1)
    with open('/home/alexarbuckle/Downloads/{}.txt'.format(arg)) as f:

        var = [i.strip() for i in f]

    os.remove('/home/alexarbuckle/Downloads/{}.txt'.format(arg))

    i, j = None, None
    l = sorted([i for i in os.listdir('/home/alexarbuckle/Desktop/Comperio') if 'Workbook' in i])
    for i in l:

        ws = xlrd.open_workbook(i).sheet_by_index(0)
        for j in range(ws.nrows):

            if (ws.cell_value(j, 0).replace(';', '') in var):

                var[var.index(ws.cell_value(j, 0).replace(';', ''))] += ';'

    if (i is None or j is None or j > 1000000):

        wb = xlwt.Workbook()
        ws = wb.add_sheet('Worksheet')
        wb.save('Workbook{}.xlsx'.format(len(l) + 1))

        j = -1
        i = 'Workbook{}.xlsx'.format(len(l) + 1)

    wb = copy(xlrd.open_workbook(i))
    ws = wb.get_sheet(0)
    for r, k in enumerate(var):

        ws.write(j + 1, r, k)

    wb.save(i)

client.run(token)
