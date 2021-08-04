# Soror by Alex Arbuckle #

import os, time, discord
from selenium import webdriver
from discord.ext import commands

id = 'Soror'
username = ''
password = ''
token = ''
client = commands.Bot(command_prefix = '{} '.format(id))

@client.command()
async def Enable(ctx):
    '''  '''

    global driver

    driver = webdriver.Chrome()

    try:

        driver.get('https://www.instagram.com/'), time.sleep(1)

        driver.find_element_by_name('username').send_keys(username), time.sleep(1)
        driver.find_element_by_name('password').send_keys(password), time.sleep(1)

        driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button').click()
        time.sleep(3), driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/section/div/button').click()
        time.sleep(3), driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

        await ctx.send('Online')

    except Exception as e:

        await ctx.send(e)

@client.command()
async def Disable(ctx):
    '''  '''

    driver.quit()

    await ctx.send('Offline')

@client.command()
async def Status(ctx):
    '''  '''

    if (driver.service.is_connectable()):

        await ctx.send('Online')

    else:

        await ctx.send('Offline')

@client.command()
async def Search(ctx, arg):
    '''  '''

    driver.get('https://www.instagram.com/{}/'.format(arg)), time.sleep(1)

    try:

        l = [arg + ';']
        var = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').get_attribute('title')

        if (int(var.replace(',', '')) < 5001):

            driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]').click(), time.sleep(2)
            for i in range((int(var.replace(',', '')) // 12) + 1):

                driver.execute_script('''var fDialog = document.querySelector('div[role="dialog"] .isgrP');
                    fDialog.scrollTop = fDialog.scrollHeight'''), time.sleep(0.25)

                for k in range(12):

                    try:

                        l.append(driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[1]/div/div[1]/div[2]/div[1]/span/a').text)

                    except:

                        l.append(driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[1]/div/div[2]/div/div/div/span/a').text)

                    time.sleep(0.2)
                    driver.execute_script('''document.querySelector("body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child(1)").remove()''')

    except Exception as e:

        print(e) # remove
        pass

    with open('{}.txt'.format(arg), 'w') as f:

        [f.write('{}\n'.format(i)) for i in l]

    await ctx.send('Frater Write {}'.format(arg), file = discord.File('/home/alexarbuckle/Desktop/Comperio/{}.txt'.format(arg), '{}.txt'.format(arg)))

    os.remove('{}.txt'.format(arg))

client.run(token)
