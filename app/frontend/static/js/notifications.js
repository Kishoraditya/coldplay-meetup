class NotificationManager {
    constructor() {
        this.notificationContainer = this.createNotificationContainer();
        this.checkPermission();
    }

    createNotificationContainer() {
        const container = document.createElement('div');
        container.className = 'notification-container';
        document.body.appendChild(container);
        return container;
    }

    async checkPermission() {
        if (Notification.permission !== 'granted') {
            await Notification.requestPermission();
        }
    }

    show(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.innerHTML = `
            <div class="notification-content">
                <p>${message}</p>
            </div>
        `;
        
        this.notificationContainer.appendChild(notification);
        
        setTimeout(() => {
            notification.classList.add('fade-out');
            setTimeout(() => {
                notification.remove();
            }, 300);
        }, 5000);
    }

    showMatch(matchData) {
        this.show(`New match with ${matchData.matched_user.name}! 🎉`, 'success');
        
        if (Notification.permission === 'granted') {
            new Notification('New Concert Buddy Match!', {
                body: `You matched with ${matchData.matched_user.name}!`,
                icon: '/static/images/logo.png'
            });
        }
    }
}

const notificationManager = new NotificationManager();
