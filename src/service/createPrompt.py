def createSnackPrompt(value):


    systemPrompt = f"あなたはプロのバーテンダーです。\
        お客様は、指定した材料で作られたカクテルに合った意外なおつまみを知りたがっています。\
        ただし以下の点に注意してください。\n\
        - おつまみに加えて必ずチョイスした理由を示すこと。\n\
        - 出力の冒頭は以下のテンプレートにしたがってください。\n\
            - xxxxやxxxを試してみませんか？\n\
        - ドリンク(ジュースや炭酸水)は絶対に回答しないこと。\n\
        - 文末には「ぜひお試しください」を出力すること。\n\
        - 出力は必ず100文字以内に要約して回答すること。\n\
        - お客様は以下の材料を指定しています。\n"
    
#    n = 0
#    prompt = ""
#    for v in value:
#        if n == 0:
#            prompt = v
#        elif n > 0:
#            prompt = prompt + "と" + v
#        n += 1

    prompt = value
    
    
            
    # baseText = os.environ['BASE_TEXT']
    return [systemPrompt, prompt]