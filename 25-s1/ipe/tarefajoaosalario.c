#include <stdio.h>

int main()
{
    int salario;
    int aumento;
    int periodototal; // criando variáveis
    
    printf("Por favor, digite um salário: ");
    scanf("%d", & salario);
    printf("Ótimo! Agora digite uma porcentagem para o aumento, mas sem o símbolo da porcentagem: ");
    scanf("%d", & aumento);
    printf("Agora,  o período de meses em que ele receberá esse aumento consecutivamente: ");
    scanf("%d", & periodototal);
    
    int periodoatual = 1;
    
    while (periodoatual != periodototal) {
    
    int salario =  salario * (int(aumento) / 100 + 1);
    periodototal++;
    }
    
    // printf("%d " "%d " "%d ", salario, aumento, periodototal); // teste, imprimindo variáveis
    return 0;
}
