// gcc -o dat_boinary -m32 -fno-stack-protector dat_boinary.c
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>



typedef struct
{
    char id[8];
    int dankness;
    char *content;
} MEME_POST;

int read_number(void)
{
    char buf[10];
    fgets(buf,10,stdin);
    return atoi(buf);
}
void secret_meme(MEME_POST *in)
{
    //l0l0l0l0l0
    in->dankness=0x69696969;
    printf("\nhere come dat boi");
    printf("\n      ,++++           ");
    printf("\n       ###+.          ");
    printf("\n        #+++          ");
    printf("\n        ++++          ");
    printf("\n      +++++++         ");
    printf("\n   ;+#, ++++'         ");
    printf("\n ,#`    +++++         ");
    printf("\n        +###'         ");
    printf("\n        +###+'        ");
    printf("\n      +##'#++         ");
    printf("\n      .#:+++#+        ");
    printf("\n      ++  ;  +        ");
    printf("\n       +` ;  +        ");
    printf("\n        +;; ++        ");
    printf("\n       `##;#++        ");
    printf("\n       #:';`+:        ");
    printf("\n      ;'`:;:+;        ");
    printf("\n      #``:;:+#        ");
    printf("\n      # `+;':#        ");
    printf("\n      #: ;'';#        ");
    printf("\n      #.`.;+`:        ");
    printf("\n      ';::;'#         ");
    printf("\n       #.:'#'         ");
    printf("\n        #+#;    o shit whaddup!");
    printf("\nsh\n");
    printf("\nit's\n");
    printf("\na\n");
    printf("\nsecret\n");
}

int main()
{
    setbuf(stdout, NULL);
    printf("\nWelcome to the meme posting center!");
    MEME_POST new_meme;
    new_meme.dankness=0; // i5 n0t v3ry d4nk
    new_meme.content=(char *)malloc(128);
    printf("\nBefore we start, please give your meme an id");
    char tmp_m3m3_id[8];
    fgets(new_meme.id,sizeof(new_meme.id)+1,stdin);
    int option=0;
    while (1)
    {
        printf("\nWhat would you like to do?");
        printf("\n1) update the id of your meme.");
        printf("\n2) Update the dankness of your m3m3.");
        printf("\n3) update the content of your maymay.");
        printf("\n4) pR1nT th3 c0nT3nT of ur memey.");
        printf("\n5) s00p3r s3cr3t meme 0pt10n.");
        printf("\n==> ");
        option = read_number();
        if (option==1)
        {
            printf("\n3nt3r ur m3m3 id");
            fread(new_meme.id,strlen(new_meme.id),1,stdin);
            new_meme.id[7] = '\0'; // 1 d0n't w4nt t0 g3t h4ck3d
        }
        else if (option==2)
        {
            printf("\n3nt3r teh d4nkn3ess 0f m3me");
            int tmp_m3m3=0;
            tmp_m3m3 = read_number();
            if (tmp_m3m3<128 && tmp_m3m3>-1)
            {
                new_meme.dankness = tmp_m3m3;
                printf("\nn0w th4t's 4 n1c3 m3m3.");
            }
            else
            {
                printf("\ntH4t's t00 d4nk.");
            }

        }
        else if (option==3)
        {
            if (new_meme.dankness>128 || new_meme.dankness<0)
            {
                printf("\nn1C3 tRy u sn34ky m3m3r.");
            }
            else
            {
                new_meme.content = fgets(new_meme.content,new_meme.dankness,stdin);
            }

        }
        else if (option==4)
        {
            printf("\nUr meme c0nT3nT:\t");
            printf("%s",new_meme.content); // U th0t 1'd g1v3 u a f0rmat m3m3 :P
        }
        else if (option==5)
        {
            secret_meme(&new_meme);
        }
    }
    free(new_meme.content);





}
