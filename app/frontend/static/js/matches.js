class MatchManager {
    constructor() {
        this.socket = new WebSocket(`wss://${window.location.host}/ws/matches`);
        this.matches = [];
        this.initializeWebSocket();
        this.setupEventListeners();
    }

    initializeWebSocket() {
        this.socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            if (data.type === 'match') {
                this.handleNewMatch(data.match);
            } else if (data.type === 'reveal') {
                this.handleContactReveal(data.match);
            }
        };
    }

    async loadMatches() {
        const response = await fetch('/api/matches', {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            }
        });
        this.matches = await response.json();
        this.renderMatches();
    }

    renderMatches() {
        const container = document.querySelector('.matches-grid');
        container.innerHTML = this.matches.map(match => `
            <div class="match-card ${match.status}" data-id="${match.id}">
                <div class="match-profile">
                    <img src="${match.matched_user.photos[0] || '/static/images/default-avatar.png'}" 
                         alt="Profile photo of ${match.matched_user.name}">
                    <h3>${match.matched_user.name}</h3>
                    <div class="match-status">
                        ${this.getStatusBadge(match.status)}
                    </div>
                    ${this.getContactInfo(match)}
                </div>
            </div>
        `).join('');
    }

    getStatusBadge(status) {
        const badges = {
            'pending': '<span class="badge pending">Pending</span>',
            'matched': '<span class="badge matched">Matched!</span>',
            'revealed': '<span class="badge revealed">Contact Revealed</span>'
        };
        return badges[status] || '';
    }

    getContactInfo(match) {
        if (match.status !== 'revealed') {
            return `<div class="reveal-countdown" data-reveal-time="${match.reveal_time}">
                        Reveals in: <span class="countdown"></span>
                    </div>`;
        }
        return `<div class="contact-info">
                    ${match.matched_user.social_links ? 
                      this.renderSocialLinks(match.matched_user.social_links) :
                      this.renderContactDetails(match.matched_user)}
                </div>`;
    }
}

// Initialize the match manager
const matchManager = new MatchManager();
