<script>
    let profilepic=document.getElementbyid("profilr-pic");
    let inputfile=document.getElementbyid("input-file");


    inputFile.onchange = function()
    {
        profilepic.src=URL.createObjectURL(inputFile.files[0])
    }
</script>