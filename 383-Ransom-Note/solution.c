/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    var randsom_counter={}
    var magazine_counter={}
    for (let i=0;i<ransomNote.length;i++){
        let x=ransomNote[i]
        randsom_counter[x]=(randsom_counter[x]||0)+1
    }
    for (let i=0;i<magazine.length;i++){
        let x=magazine[i]        
        magazine_counter[x]=(magazine_counter[x]||0)+1   
    }
    console.log(ransomNote,magazine,randsom_counter,magazine_counter)
    for (let x in randsom_counter ){
        let count=randsom_counter[x];
        if ((magazine_counter[x]||0)<count)
            return false 
    }
    return true;
    
    
};