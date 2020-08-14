# manchetes-lib-python
O manchetes-lib-python tem como objetivo uma fácil utilização da [API Rest de manchetes](https://github.com/lucastheo/manchetes), com essa implementação quero disponibilizar informações de diversor portais de noticias no Brasil.



### Exeplo de uso
Nesse caso a classe faz o acesso as API Rest buscando a informações de palavras mais citadas por dia e data

```
1    most_cited = MostCited()
2    for url, data in most_cited.keys_tuples():
3       print( most_cited.find(url,data) )
```
O que vai sair na sysout do sistema é um print de um dict
```
{
    'exemplo': 50,
    'teste': 46,
    'manchetes': 40
}
```