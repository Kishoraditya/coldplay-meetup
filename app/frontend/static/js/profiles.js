class ProfileManager {
    constructor() {
        this.profiles = [];
        this.currentSection = null;
        this.initializeEventListeners();
    }

    async loadProfiles(section) {
        try {
            const response = await fetch(`/api/profiles/section/${section}`, {
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('token')}`
                }
            });
            
            if (!response.ok) throw new Error('Failed to load profiles');
            
            this.profiles = await response.json();
            this.renderProfiles();
        } catch (error) {
            console.error('Error loading profiles:', error);
            this.showError('Failed to load profiles. Please try again.');
        }
    }

    renderProfiles() {
        const container = document.querySelector('.profile-grid');
        container.innerHTML = this.profiles.map(profile => `
            <div class="profile-card" data-id="${profile.id}">
                <div class="profile-image">
                    <img src="${profile.photos[0] || '/static/images/default-avatar.png'}" 
                         alt="Profile photo of ${profile.name}">
                </div>
                <h3>${profile.name}</h3>
                <div class="profile-details">
                    <p>${profile.purpose}</p>
                    <p>Section: ${profile.seat_section}</p>
                    ${profile.age ? `<p>Age: ${profile.age}</p>` : ''}
                </div>
                <button class="match-button" onclick="profileManager.likeProfile(${profile.id})">
                    Meet Up
                </button>
            </div>
        `).join('');
    }

    async likeProfile(profileId) {
        try {
            const response = await fetch(`/api/matches/like/${profileId}`, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('token')}`
                }
            });
            
            if (!response.ok) throw new Error('Failed to like profile');
            
            const result = await response.json();
            if (result.status === 'matched') {
                this.showMatchNotification(profileId);
            }
        } catch (error) {
            console.error('Error liking profile:', error);
        }
    }
}

const profileManager = new ProfileManager();
