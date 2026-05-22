# %% 

from random import randint
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

valor_pacote = 20
valor_album = 80
qtde_pacote = 20
qtde_album = 180

# %%

def completa_album(qtde_album=980, qtde_pacote=7):
    album = set()

    count = 0
    while len(album) < qtde_album:
            pacote = {randint(1, qtde_album) for i in range(qtde_pacote)}
            album = album.union(pacote)
            count += 1

    return count
# %%

albuns = [completa_album() for i in range (1000)]
albuns

# %%

plt.hist(albuns, color= 'Purple')
plt.xlabel('Pacotes')
plt.ylabel('Quantidade albuns')
plt.title("Histograma de Albuns completos")
plt.grid(True)

# %%
 
mediana = pd.Series(albuns).median()

valor_total_pacote = mediana * valor_pacote

valor_total = valor_total_pacote + valor_album

print(f'Valor estimado de gasto em pacotes: R${valor_total_pacote:.2f}')
print(f'Valor total gasto (Pacotes e Álbum): R${valor_total}')


# %%
# Agora com amigos

def completa_albuns(qtde_album=180, qtde_pacote=6, N=2):
   
    albuns = [set() for i in range(N)]
    count = 0

    while min([len(a) for a in albuns]) < qtde_album:
        pacote = [randint(1, qtde_album) for i in range(qtde_pacote)]
        count += 1

        for f in pacote.copy():

            for album in albuns:
                if f not in album:
                    album.add(f)
                    pacote.remove(f)
                    break
    return count

df = pd.DataFrame()

for j in range(1, 9):
    print(f'Processando Álbum collab = {j}...')
    df[f'albuns_collab_{j}'] = [completa_albuns(N=j)/j for i in range(1000)]

df
# %%

df_status = df.median().reset_index().rename(columns={
     "index": "Collabs",
     0 : "Qtde Pacotes",
})

df_status['Valor'] = df_status["Qtde Pacotes"] * valor_pacote + valor_album
df_status['Qtde Pessoas'] = df_status['Collabs'].apply(lambda x: int(x.split("_")[-1]))
df_status   

# %%

sns.barplot(df_status, x="Qtde Pessoas", y="Valor", palette='rainbow')
plt.grid(True)
plt.suptitle("Valor para completar bide pokemon")
plt.title("Album = 180 / Pacote = 6")
