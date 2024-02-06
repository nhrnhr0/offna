

export function timeduration_to_hebrew_string(duration) {
    const secounds = Math.floor(duration / 1000);
    const minutes = Math.floor(secounds / 60);
    const hours = Math.floor(minutes / 60);
    const days = Math.floor(hours / 24);
    const weeks = Math.floor(days / 7);
    const months = Math.floor(weeks / 4);
    const years = Math.floor(months / 12);
    if (years > 0) {
        if (years === 1) {
            return 'שנה';
        }
        return years + ' שנים';
    }
    if (months > 0) {
        if (months === 1) {
            return 'חודש';
        }
        return months + ' חודשים';
    }
    if (weeks > 0) {
        if (weeks === 1) {
            return 'שבוע';
        }
        return weeks + ' שבועות';
    }
    if (days > 0) {
        if (days === 1) {
            return 'יום';
        }
        return days + ' ימים';
    }
    if (hours > 0) {
        if (hours === 1) {
            return 'שעה';
        }
        return hours + ' שעות';
    }
    if (minutes > 0) {
        if (minutes === 1) {
            return 'דקה';
        }
        return minutes + ' דקות';
    }
    if (secounds > 0) {
        if (secounds === 1) {
            return 'שניה';
        }
        return secounds + ' שניות';
    }
    return '0 שניות';
}