console.log('1')



b = new Promise((resolve, reject) => {
    a = setTimeout(()=>{
        console.log('from promise')
    },0)
    resolve()
})
a = setTimeout(()=>{
    console.log('from timeout')
},0)


console.log('2')