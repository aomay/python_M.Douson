#таблица рекорддов с записью в файл records.txt
import pickle

def scs_plus(sc, name, scores):
    '''добавляет или заменят счет игрока'''
    names = []
    for k in range(len(scores)):
        names.append(scores[k][1])
    if name in names:
        print('уже есть в списке')
        for n in range(len(scores)):
            if scores[n][1] == name and scores[n][0] < sc:
                del scores[n]
                print('рекорд заменен')
                scores.append((sc, name))
    else:
        scores.append((sc, name))
    return scores

def show_score(scores):
    print('\t----------------------')
    print('\t имя\t\t счет')
    print('\t----------------------')
    for n in scores:
        print ('\t', n[1], '\t\t', n[0])
    print('\t----------------------')

def main(score):
    name = input('введите своё имя: ')

    try:
        recs = open('records.dat', 'rb')
    except:
        recs = open('records.dat', 'wb')
        pickle.dump([], recs)
        recs.close()
        recs = open('records.dat', 'rb')

    scores = pickle.load(recs)
    recs.close()

    scores = scs_plus(score, name, scores)
    scores.sort(reverse = True)
    scores = scores[:5]

    show_score(scores)

    recs = open('records.dat', 'wb')
    pickle.dump(scores, recs)
    recs.close()



score = int(input('счет: '))
main(score)
