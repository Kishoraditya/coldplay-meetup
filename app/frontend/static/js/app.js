document.addEventListener('alpine:init', () => {
    Alpine.data('profileManager', () => ({
        profiles: [],
        loading: false,
        
        async init() {
            await this.loadProfiles()
        },
        
        async loadProfiles() {
            this.loading = true
            try {
                const response = await fetch('/api/profiles', {
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('token')}`
                    }
                })
                this.profiles = await response.json()
            } catch (error) {
                console.error('Failed to load profiles:', error)
            }
            this.loading = false
        },
        
        async createMatch(profileId) {
            try {
                const response = await fetch(`/api/match/${profileId}`, {
                    method: 'POST',
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('token')}`
                    }
                })
                const result = await response.json()
                if (result.status === 'matched') {
                    this.showMatchNotification()
                }
            } catch (error) {
                console.error('Failed to create match:', error)
            }
        }
    }))
})
