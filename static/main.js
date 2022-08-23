let timer = document.getElementById('timer')
let form = document.getElementById('exam_form')

let minute = 18
let now = new Date().getTime()
let final = now + minute * 1000 * 60


function timeFormat(distance){
    let minutes = Math.floor(distance / (1000 * 60))
    let seconds = Math.floor((distance % (1000 * 60)) / 1000)

    if (minutes == 0){
        timer.innerHTML = `${seconds}s`
    }else{
        timer.innerHTML = `${minutes}m ${seconds}s`
    }
    return [minutes, seconds]
}

timeFormat(final - now)

interval = setInterval(()=>{
    let now = new Date().getTime()
    let distance = final - now;
    [minutes, seconds] = timeFormat(distance)
    if (seconds == 0 && minutes == 0){
        clearInterval(interval)
        form.submit()
    }
}, 1000)


