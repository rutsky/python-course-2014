import win32com.client

def search_replace_all(word_file, find_str, replace_str):
    '''Заменить строку find_str на строку replace_str в word_file'''
    wdFindContinue = 1
    wdReplaceAll = 2

    # Создаём COM-объект
    app = win32com.client.DispatchEx("Word.Application")
    app.Visible = 0
    app.DisplayAlerts = 0
    app.Documents.Open(word_file)

    # expression.Execute(FindText, MatchCase, MatchWholeWord,
    #   MatchWildcards, MatchSoundsLike, MatchAllWordForms, Forward, 
    #   Wrap, Format, ReplaceWith, Replace)
    app.Selection.Find.Execute(find_str, False, False, False, False, False, \
        True, wdFindContinue, False, replace_str, wdReplaceAll)
    app.ActiveDocument.Close(SaveChanges=True)
    app.Quit()

f = 'c:/path/to/my/word.doc'
search_replace_all(f, 'string_to_be_replaced', 'replacement_str')
