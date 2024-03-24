import java.util.Arrays;

public class OrdenacaoCrescente {
    public static void main(String[] args) {
        int[] numeros = {5, 2, 9, 1, 5, 6};

        System.out.println("Array original: " + Arrays.toString(numeros));

        ordenarCrescente(numeros);

        System.out.println("Array ordenado em ordem crescente: " + Arrays.toString(numeros));
    }

    public static void ordenarCrescente(int[] arr) {
        int n = arr.length;
        boolean troca;

        do {
            troca = false;

            for (int i = 0; i < n - 1; i++) {
                if (arr[i] > arr[i + 1]) {
                    // Trocar os elementos se estiverem na ordem errada
                    int temp = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = temp;

                    troca = true;
                }
            }

            // Após uma passagem completa, o maior elemento está no final, então reduzimos n
            n--;
        } while (troca);
    }
}
