var ptr=""

for(i=1;i<=7;i++){
    for(j=1;j<=5;j++){
        if(i==1||i==4||i==7||(j==1&&i<=4)||(j==5&&i>=4))
            ptr+="*"
        else
            ptr+=" "
    }

    ptr+="\n"
}
