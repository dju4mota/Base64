# Base64

## O que é?
Base64 é um algoritmo de codificação que permite transformar qualquer caracter em um alfabeto que consiste de letras do alfabeto latino, números, + e /. Graças a ele, você pode converter caracteres chineses, emojis e até mesmo imagens em uma string legível, que pode ser salva ou transferida para qualquer lugar.

## Como funciona?

O algoritmo pode ser dividido em três etapas, que são:
1. Transformar os caracteres em bytes
2. Converter os bytes para usar 6 bits
3. Converter os 6 bits para um número decimal da tabela 64 

E para trabalhar com imagens, tem-se a etapa extra de converter os pixels em bytes.

## Porque utilizar Base64 ? 

Para entender o porquê da criação do Base64, imagine que durante uma ligação telefônica Alice quer mandar uma imagem para Bob. O primeiro problema é que ela não pode simplesmente descrever como é a imagem, porque Bob precisa de uma cópia exata. Nesse caso, Alice pode converter a imagem em sistema binário e ditar para Bob os dígitos binários (bits), e depois ele poderá convertê-los de volta para a imagem original. O segundo problema é que as tarifas telefônicas são muito caras e ditar cada byte com 8 dígitos binários iria levar muito tempo. Para reduzir custos, Alice e Bob concordam em utilizar um método mais simples para transferência de dados utilizando um alfabeto especial, que substitui cada 6 dígitos por uma letra. Essa combinação permite que o dado não seja modificado na transferência entre os sistemas de informação, como o email, que não eram tradicionalmente 8 bit-clean.

## História 

A história do Base64 começou muito tempo atrás, quando os engenheiros ainda discutiam quantos bits deveriam formar um byte. Agora nós utilizamos bytes de 8 bits, mas antes eram utilizados 7 bits, 6 bits e até mesmo 3 bits. Quando a codificação em 8 bits foi aprovada como padrão, muitos sistemas ainda utilizavam codificações antigas e não tinhm suporte para o "novo padrão". Isso acabou gerando o fato de que alguns dados simplesmente foram perdidos durante a transferência entre os sistemas novos e antigos.

## Pontos Fortes

* É um algoritmo de codificação simples e fácil de implementar
* É um algoritmo de codificação que permite transformar qualquer caracter em um alfabeto que consiste de letras do alfabeto latino, números, + e /
* Muito útil em ambientes onde pode se transportar dados apenas com textos 
* Evita que os dados sejam alterados devido a diferenças entre padrões do tamanho do byte

## Pontos Fracos

* O tamanho do arquivo codificado é maior que o original, compensando apenas para arquivos pequenos
* Não é seguro, pois qualquer pessoa pode decodificar o arquivo
