
    def kofaktor_bul():
        liste2.append(
            liste[5] * (liste[10] * liste[15] - liste[14] * liste[11])
            - liste[6] * (liste[9] * liste[15] - liste[13] * liste[11])
            + liste[7] * (liste[9] * liste[14] - liste[13] * liste[10])
        )

        liste2.append(
            -1 * (
                    liste[4] * (liste[10] * liste[15] - liste[14] * liste[11])
                    - liste[6] * (liste[8] * liste[15] - liste[12] * liste[11])
                    + liste[7] * (liste[8] * liste[14] - liste[12] * liste[10])
            )
        )

        liste2.append(
            liste[9] * (liste[10] * liste[15] - liste[14] * liste[11])
            - liste[5] * (liste[8] * liste[15] - liste[12] * liste[11])
            + liste[7] * (liste[8] * liste[13] - liste[12] * liste[9])
        )

        liste2.append(
            -1 * (
                    liste[4] * (liste[9] * liste[14] - liste[13] * liste[10])
                    - liste[5] * (liste[8] * liste[14] - liste[12] * liste[10])
                    + liste[6] * (liste[8] * liste[13] - liste[12] * liste[9])
            )
        )

        liste2.append(
            liste[1] * (liste[10] * liste[15] - liste[14] * liste[11])
            - liste[2] * (liste[9] * liste[15] - liste[13] * liste[11])
            + liste[3] * (liste[9] * liste[14] - liste[13] * liste[10])
        )

        liste2.append(
            liste[0] * (liste[10] * liste[15] - liste[14] * liste[11])
            - liste[2] * (liste[8] * liste[15] - liste[12] * liste[11])
            + liste[3] * (liste[8] * liste[14] - liste[12] * liste[10])
        )

        liste2.append(
            -1 * (
                    liste[0] * (liste[9] * liste[15] - liste[13] * liste[11])
                    - liste[1] * (liste[8] * liste[15] - liste[12] * liste[11])
                    + liste[3] * (liste[8] * liste[13] - liste[12] * liste[9])
            )
        )

        liste2.append(
            liste[0] * (liste[9] * liste[14] - liste[13] * liste[10])
            - liste[1] * (liste[8] * liste[14] - liste[12] * liste[10])
            + liste[2] * (liste[8] * liste[13] - liste[12] * liste[9])
        )

        liste2.append(
            -1 * (
                    liste[1] * (liste[6] * liste[15] - liste[7] * liste[14])
                    - liste[2] * (liste[5] * liste[15] - liste[13] * liste[7])
                    + liste[3] * (liste[5] * liste[14] - liste[13] * liste[6])
            )
        )

        liste2.append(
            liste[0] * (liste[6] * liste[15] - liste[14] * liste[7])
            - liste[2] * (liste[4] * liste[15] - liste[12] * liste[7])
            + liste[3] * (liste[4] * liste[14] - liste[12] * liste[6])
        )

        liste2.append(
            -1 * (
                    liste[0] * (liste[5] * liste[15] - liste[13] * liste[7])
                    - liste[1] * (liste[4] * liste[15] - liste[12] * liste[7])
                    + liste[3] * (liste[4] * liste[13] - liste[12] * liste[5])
            )
        )

        liste2.append(
            liste[0] * (liste[5] * liste[14] - liste[6] * liste[13])
            - liste[1] * (liste[4] * liste[14] - liste[12] * liste[6])
            + liste[2] * (liste[4] * liste[13] - liste[12] * liste[5])
        )

        liste2.append(
            -1 * (
                    liste[1] * (liste[6] * liste[11] - liste[10] * liste[7])
                    - liste[2] * (liste[5] * liste[11] - liste[9] * liste[7])
                    + liste[3] * (liste[5] * liste[10] - liste[9] * liste[6])
            )
        )

        liste2.append(
            liste[0] * (liste[6] * liste[11] - liste[10] * liste[7])
            - liste[2] * (liste[4] * liste[11] - liste[8] * liste[7])
            + liste[3] * (liste[4] * liste[10] - liste[8] * liste[6])
        )

        liste2.append(
            -1 * (
                    liste[0] * (liste[5] * liste[11] - liste[9] * liste[7])
                    - liste[1] * (liste[4] * liste[11] - liste[8] * liste[7])
                    + liste[3] * (liste[4] * liste[9] - liste[8] * liste[5])
            )
        )

        liste2.append(
            liste[0] * (liste[5] * liste[10] - liste[9] * liste[6])
            - liste[1] * (liste[4] * liste[10] - liste[8] * liste[6])
            + liste[2] * (liste[4] * liste[9] - liste[8] * liste[5])
        )
        transpoze_bul()


    def transpoze_bul():
        liste3.append(liste2[4])
        liste3.append(liste2[8])
        liste3.append(liste2[12])
        liste3.append(liste2[1])
        liste3.append(liste2[5])
        liste3.append(liste2[9])
        liste3.append(liste2[13])
        liste3.append(liste2[2])
        liste3.append(liste2[6])
        liste3.append(liste2[10])
        liste3.append(liste2[14])
        liste3.append(liste2[3])
        liste3.append(liste2[7])
        liste3.append(liste2[11])
        liste3.append(liste2[15])
        ekmatris_yazdir()
    def ekmatris_yazdir():
        for i in range(0, len(liste3), 4):
            print(liste3[i:i + 4])
    kofaktor_bul()
